from crewai import Task

class TasksFactory:
    def create_analysis_task(self, agent, input_user: str) -> Task:
        return Task(
            description=(
                f"Here is the request or raw data: '{input_user}'. "
                "Your goal is to extract three key pieces of information from it. "
                "If the user mentions a file name, use your tool to read its content. "
                "If the user provided the text directly, do not use the tool and simply analyze the provided text. "
                "Your final deliverable must be in French."
            ),
            expected_output="A summary of the three key pieces of information extracted, written in French.",
            agent=agent
        )

    def create_planning_task(self, agent) -> Task:
        return Task(
            description=(
                "Based on the information extracted by the analyst, "
                "write a 3-step macro strategic action plan. "
                "Your final deliverable must be in French."
            ),
            expected_output="A strategic action plan in 3 steps, written in French.",
            agent=agent
        )
