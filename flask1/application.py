from bankapp import create_app

application = create_app()

if __name__ == "__main__":
	
	application.debug = True
	application.run()
	