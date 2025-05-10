from crewai import Crew, Task
from agents import create_mba_advisor


class MBACrew:
    def __init__(self):
        self.advisor = create_mba_advisor()

    def create_task(self, question: str) -> Task:
        return Task(
            description=question,
            expected_output="Accurate, well-structured MBA program answer.",
            agent=self.advisor
        )

    def run(self, question: str):
        task = self.create_task(question)
        crew = Crew(
            agents=[self.advisor],
            tasks=[task],
            verbose=True
        )
        return crew.kickoff()
