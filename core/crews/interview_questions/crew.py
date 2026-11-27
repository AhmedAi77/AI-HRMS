
from crewai import Agent, Process, Task, Crew
from  crewai.project import CrewBase, agent, crew, task
from core.tools import basic_llm

@CrewBase
class InterviewQuestionsCrew(CrewBase):
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

@agent
def interview_question_agent(self)->Agent:
    return Agent(
        config=self.agents_config["interview_question_generator"],
        verbose=True,
        llm=basic_llm,
    )

@task
def interview_question_task(self)->Task:
    return Task(
        config=self.tasks_config["interview_question_task"],
    )

@crew
def crew(self)->Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True,
    )