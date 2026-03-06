#.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y final_project || :
	@pip install -e .

run_load_data:
	python -c 'from final_project.main import load_data; load_data(".")'

run_preprocess:
	python -c 'from final_project.main import preprocess; preprocess(".", 0.3)'

run_train:
	python -c 'from final_project.main import train; train(".")'

run_evaluate:
	python -c 'from final_project.main import evaluate; evaluate(".")'

run_pred:
	python -c 'from final_project.main import pred; pred(".")'

run_all: run_load_data run_preprocess run_train run_evaluate run_pred

#run_workflow:
#	PREFECT__LOGGING__LEVEL=${PREFECT_LOG_LEVEL} python -m final_project.interface.workflow

#run_api:
#	uvicorn final_project.api.fast:app --reload
