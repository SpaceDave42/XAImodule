from util import loadDataset, convertObjectColumnDatatypesToCategory
from XAI_adapters.XAI_toolbox_adapter import explainXAIToolbox

X, Y, target, features = loadDataset("datasets/college_working_tabular_regression.csv", "datasets/college_configuration.json")
X = convertObjectColumnDatatypesToCategory(X)

explainXAIToolbox(X, Y, target, "College", remove_plots=True)

X, Y, target, features = loadDataset("datasets/titanic_working_tabular_classification.csv", "datasets/titanic_working_configuration.json")
X = convertObjectColumnDatatypesToCategory(X)

explainXAIToolbox(X, Y, target, "Titanic", remove_plots=True)
