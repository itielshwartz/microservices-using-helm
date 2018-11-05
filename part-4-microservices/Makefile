run:
	kubectl apply \
  	-f db_service_wrapper/service.yaml -f db_service_wrapper/deployment.yaml
	sleep 5 && \
	kubectl apply 	-f backend/deployment.yaml  && \
	kubectl get pods