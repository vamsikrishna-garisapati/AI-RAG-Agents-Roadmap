# Multi-Agent Orchestration System

class Agent:
    def __init__(self, name):
        self.name = name

    def act(self):
        return f'{self.name} is acting.'

class Orchestrator:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def coordinate_actions(self):
        actions = []
        for agent in self.agents:
            actions.append(agent.act())
        return actions

# Example usage:
if __name__ == '__main__':
    agent1 = Agent('Agent 1')
    agent2 = Agent('Agent 2')

    orchestrator = Orchestrator()
    orchestrator.add_agent(agent1)
    orchestrator.add_agent(agent2)

    results = orchestrator.coordinate_actions()
    for result in results:
        print(result)