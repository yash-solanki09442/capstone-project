import pytest


@pytest.mark.django_db
def test_task_update_triggers_realtime_event(api_client, task, mocker):

    mock_broadcast = mocker.patch("tasks.views.broadcast_event")

    mocker.patch("tasks.views.transaction.on_commit", side_effect=lambda fn: fn())

    url = f"/api/tasks/{task.id}/"
    response = api_client.patch(url, {"status": "done"}, format="json")

    assert response.status_code == 200

    mock_broadcast.assert_called_once()
    event = mock_broadcast.call_args.args[0]

    assert event["payload"]["status"] == "done"
    assert event["type"] == "task.updated"
    assert event["task_id"] == task.id
    assert event["project_id"] == task.project_id
    assert "payload" in event


@pytest.mark.django_db
def test_invalid_update_does_not_trigger_broadcast(api_client, task, mocker):
    mock_broadcast = mocker.patch("tasks.views.broadcast_event")
    mocker.patch("tasks.views.transaction.on_commit", side_effect=lambda fn: fn())

    url = f"/api/tasks/{task.id}/"
    res = api_client.patch(url, {"status": "invalid"}, format="json")

    assert res.status_code == 400
    mock_broadcast.assert_not_called()
