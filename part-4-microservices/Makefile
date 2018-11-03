run:
	kubectl apply -f backend/deployment.yaml -f db_service_wrapper/deployment.yaml -f db_service_wrapper/service.yaml && sleep 5 && kubectl port-forward $$(kubectl get pod -l name=main -o jsonpath='{.items[0].metadata.name}') 8080:8080
