if __name__ == '__main__':
	agent = ModelBasedVacuumAgent()
	environment = VacuumEnvironment()
	environment.add_thing(agent)
	environment.run()
	environment.status == {(1, 0): 'Clean' , (0, 0): 'Clean'}
