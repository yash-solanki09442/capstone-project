class ReportService:
    def generate(self, data: list[int]) -> str:
        total = sum(data)
        return f"Total: {total}"

    def save_to_file(self, report: str, path: str) -> None:
        with open(path, "w") as f:
            f.write(report)
