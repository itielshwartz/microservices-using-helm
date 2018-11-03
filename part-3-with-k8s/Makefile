run:
	kubectl apply -f deployment.yaml && kubectl port-forward $$(kubectl get pod -l name=main -o jsonpath='{.items[0].metadata.name}') 5000:5000
