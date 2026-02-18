class ReportGenerator:
    def generate(self, data: list[int]) -> str:
        return f"Total: {sum(data)}"


class FileReportRepository:
    def save(self, report: str, path: str) -> None:
        with open(path, "w") as f:
            f.write(report)
