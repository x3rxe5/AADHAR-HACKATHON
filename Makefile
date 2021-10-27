run-db:
	docker run --name fastapi_postgres -p 5432:5432 -e POSTGRES_PASSWORD=test123 -e POSTGRES_DB=aadhar -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
