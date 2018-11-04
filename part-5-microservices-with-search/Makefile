run:
	kubectl apply -f backend/deployment.yaml -f db_service_wrapper/deployment.yaml -f db_service_wrapper/service.yaml\
	&& sleep 1\
	&& kubectl port-forward $$(kubectl get pod  --field-selector=status.phase==Running -l name=main -o jsonpath='{.items[0].metadata.name}') 8080:8080