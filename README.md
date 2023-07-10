## Live application Links :octopus:

- Please use this application responsibly, as we have limited free credits remaining.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](http://35.231.47.220:30006/)

[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=12dn3Hs3BN9EUdLaln8LcXcGW6GwyTEJBKvV6ACbZrAk)



## Problem Statement :memo:
How to leverage azure cognitive vision science kit which is model as a service for a visual search with an given image and prompt.

## Project Goals :dart:
**Task -1:** 
1. Executing azure vision workshop reference notebook from 6 to 10 with gradio app.

**Task -2:** 
1. Convert the ipynb notebooks and architect it as a Python streamlit application.
2. Dockerize the model as a service and deploy on GCP.


## Technologies Used :computer:
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoft-azure&style=for-the-badge&logoColor=white)](https://azure.microsoft.com)
![gcp provider](https://img.shields.io/badge/GCP-orange?style=for-the-badge&logo=google-cloud&color=orange)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Codelabs](https://img.shields.io/badge/Codelabs-violet?style=for-the-badge)

## Data Source :flashlight:
1. https://www.dropbox.com/s/f5983zo3etaqap9/fashion_samples.zip

## Requirements
```
streamlit==1.22.0
python-dotenv
numpy==1.24
nomic
matplotlib
seaborn
cleanvision
plotly
scikit-learn
umap-learn
```


## How to run Application locally
To run the application locally, follow these steps:
1. Clone the repository to get all the source code on your machine.

2. Install docker desktop on your system

3. Create a .env file in the root directory with the following variables:
    ``` 
   # Azure Vision Variables
   azure_cv_key=
   azure_cv_endpoint=

   atlas_nomic_key=
    ```

4. Once you have set up your environment variables, Start the application by executing
    ``` 
   Make build-up
    ```

5. Once all the docker containers spin up, Access the application at following links
    ``` 
   Stremlit UI: http://localhost:30006/
    ```

6. To delete all active docker containers execute
    ``` 
   Make down
    ``` 


## References
1. Azure Vision Notebooks - https://github.com/Azure/gen-cv/tree/main/azure_computer_vision_workshop


## Learning Outcomes
1. How to leverage model as a service
2.

## Team Information and Contribution
Name | Contributions 
--- | --- |
Sanjana Karra | Designed streamlit interface for prompt based visual search, Deployed the application on GCP
Nikhil Reddy Polepally | Designed streamlit interface for image based similarity search, storing  embeddings.
Shiva Sai Charan Ruthala | Executing Azure Vision workshop notebooks 06 to 10, Displaying Image Catalog and dataset analysis with a specific image analysis
