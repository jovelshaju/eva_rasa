# eva

## code to run Rasa server for API

rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"


## EValuation Code

rasa test nlu --config configs/config-orig.yml --cross-validation --runs 1 --folds 2 --out results/config-orig

## View Result Analysis

streamlit run viewresults.py