# eva

## code to run Rasa server for API

rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"

## EValuation Code

rasa test nlu --config configs/config-mega-basic.yml --cross-validation --runs 1 --folds 2 --out results/config-mega-basic-crf
rasa test nlu --config configs/config-mega-basic.yml --cross-validation --runs 1 --folds 2 --out results/config-mega-basic
rasa test nlu --config configs/config-orig.yml --cross-validation --runs 1 --folds 2 --out results/config-orig
rasa test nlu --config configs/diet-heavy.yml --cross-validation --runs 1 --folds 2 --out results/diet-heavy
rasa test nlu --config configs/diet-light.yml --cross-validation --runs 1 --folds 2 --out results/diet-light
rasa test nlu --config configs/diet-replace-mask.yml --cross-validation --runs 1 --folds 2 --out results/diet-replace-mask
rasa test nlu --config configs/diet-replace.yml --cross-validation --runs 1 --folds 2 --out results/diet-replace

## View Result Analysis

streamlit run viewresults.py

