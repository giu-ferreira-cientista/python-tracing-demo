build:
	docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
	
up:
	docker-compose up --build
