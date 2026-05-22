from crewai import Crew, Process
from src.agents.agents_factory import AgentsFactory
from src.tasks.tasks_factory import TasksFactory

def main():
    print("--- CrewAI Multi-Agent System (Local) ---")

    # 1. Create the test file programmatically
    with open("document_test.txt", "w", encoding="utf-8") as f:
        f.write("Projet X : Lancement prévu en septembre.\n")
        f.write("Budget alloué : 50k.\n")
        f.write("Problème actuel : manque de personnel.\n")

    # 2. Get user input
    user_input = input("Veuillez saisir votre demande (texte direct ou nom de fichier) : ")

    # 3. Instantiate factories
    agents_factory = AgentsFactory()
    tasks_factory = TasksFactory()

    # 4. Create agents
    analyst = agents_factory.create_data_analyst()
    planner = agents_factory.create_strategic_planner()

    # 5. Create tasks
    analysis_task = tasks_factory.create_analysis_task(analyst, user_input)
    planning_task = tasks_factory.create_planning_task(planner)

    # 6. Instantiate the Crew
    crew = Crew(
        agents=[analyst, planner],
        tasks=[analysis_task, planning_task],
        process=Process.sequential,
        verbose=True
    )

    # 7. Kickoff
    print("\n--- Starting the Crew ---")
    result = crew.kickoff()

    print("\n--- Final Result ---")
    print(result)

if __name__ == "__main__":
    main()
