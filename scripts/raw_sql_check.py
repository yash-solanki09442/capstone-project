import os

import psycopg2


def main() -> None:
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "capstone"),
        user=os.getenv("DB_USER", "capstone"),
        password=os.getenv("DB_PASSWORD", "capstone"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
    )

    try:
        with conn.cursor() as cur:
            # This table name is the Django default: <appname>_<modelname>
            # If your app names are projects/tasks/comments, tables usually become:
            # projects_project, tasks_task, comments_comment
            cur.execute("""
                SELECT id, title, slug, created_at
                FROM projects_project
                ORDER BY created_at DESC
                LIMIT 10;
                """)
            rows = cur.fetchall()

            print("\nLatest Projects:")
            for row in rows:
                print(row)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
