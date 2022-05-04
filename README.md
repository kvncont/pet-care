# Pet Care API
API Demo created with [FastAPI](https://fastapi.tiangolo.com/) + [CosmosDB](https://azure.microsoft.com/es-es/free/cosmos-db/)

# Table of Contents
1. [Run locally](#run-locally)
2. [Run as Container](#run-as-container)
3. [Run on Kubernetes](#run-on-kubernetes)

## Run locally
```bash
# Install virtual environment (In case you don't have it)
pip install virtualenv

# Create the virtual environment
## OSX / Linux(Bash)
virtualenv venv

## Windows
python -m venv venv

# Activate virtual environment
## OSX / Linux(Bash)
venv/bin/activate

## CMD
venv\Scripts\Activate.bat

## Powershell
venv\Scripts\Activate.ps1

## Bash Shell
. ./venv/Scripts/activate

# Create the environment variables
## OSX / Linux(Bash)
export COSMOS_URI="xxxxxxxxxxxxxxxxxxxxxxxx"
export COSMOS_KEY="xxxxxxxxxxxxxxxxxxxxxxxx"
export COSMOS_DB="xxxxxxxxxxxxxxxxxxxxxxxxx"
export COSMOS_CONTAINER="xxxxxxxxxxxxxxxxxx"

## Windows (Powershell)
$Env:COSMOS_URI="xxxxxxxxxxxxxxxxxxxxxxxxxx"
$Env:COSMOS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxx"
$Env:COSMOS_DB="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
$Env:COSMOS_CONTAINER="xxxxxxxxxxxxxxxxxxxx"

# Download dependencies
pip install --no-cache-dir --upgrade -r requirements.txt

# Run the uvicorn server
uvicorn app.main:app --port 8000 --reload


# Deactivate virtual environment
# (Optional - In case you want to deactivate the virtual environment)
deactivate
```

## Run as container
```bash
# Build the image
docker build -t pet-care:1.0 .

# Create the environment variables
# OSX / Linux(Bash)
export COSMOS_URI="xxxxxxxxxxxxxxxxxxxxxxxx"
export COSMOS_KEY="xxxxxxxxxxxxxxxxxxxxxxxx"
export COSMOS_DB="xxxxxxxxxxxxxxxxxxxxxxxxx"
export COSMOS_CONTAINER="xxxxxxxxxxxxxxxxxx"

# Windows (Powershell)
$Env:COSMOS_URI="xxxxxxxxxxxxxxxxxxxxxxxxxx"
$Env:COSMOS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxx"
$Env:COSMOS_DB="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
$Env:COSMOS_CONTAINER="xxxxxxxxxxxxxxxxxxxx"

# Run the container
docker run --name pet-care --rm -d -p 8000:8000 -e COSMOS_URI -e COSMOS_KEY -e COSMOS_DB -e COSMOS_CONTAINER pet-care:1.0
```

## Run on kubernetes
```bash
# Build the image
docker build -t myregistry/pet-care:1.0 .

# Push the image to the registry
docker push myregistry/pet-care:1.0

# Change the configmap values (Use your cosmos account values)
kubectl apply -f k8s/dev/.
```

## Usage Example

### Test API (Endpoints)

```bash
# Docs (Swagger)
http://127.0.0.1:8000/docs

# Docs (ReDoc)
http://127.0.0.1:8000/redoc

# Find all pets (GET)
http://127.0.0.1:8000/pets

# Find pet by id (GET
http://127.0.0.1:8000/pet/{id}

# Delete pet by id (DELETE)
http://127.0.0.1:8000/pet/{id}

# Upsert pet (PUT)
http://127.0.0.1:8000/pet

```

### JSON Body (PUT)
```json
{
  "name": "Doki",
  "birthday": "2019-11-01",
  "is_alive": false,
  "breed": "Poodle",
  "gender": "Male",
  "color": "Champang",
  "owners": [
    {
      "id": "000000000",
      "name": "Beatriz",
      "last_name": "Pinzón",
      "address": {
        "country": "Colombia",
        "city": "Bogotá"
      },
      "contact": {
        "email": "Beatriz@example.com",
        "phone": "88448844"
      }
    }
  ],
  "vaccines": [
    {
      "vet": "Marcela Valencia",
      "product": "Vanguard Plus 5",
      "date": "2019-12-15",
      "next_vaccine_date": "2020-01-15"
    },
    {
      "vet": "Marcela Valencia",
      "product": "Canigen L",
      "date": "2020-01-18",
      "next_vaccine_date": "2020-02-18"
    },
    {
      "vet": "Marcela Valencia",
      "product": "Hipradog 7",
      "date": "2020-02-22",
      "next_vaccine_date": "2020-03-18"
    },
    {
      "vet": "Marcela Valencia",
      "product": "Vanguard Plus 5 L4",
      "date": "2020-03-21",
      "next_vaccine_date": "2020-04-21"
    },
    {
      "vet": "Marcela Valencia",
      "product": "Defensor 1",
      "date": "2020-05-09",
      "next_vaccine_date": "2020-06-20"
    },
    {
      "vet": "Marcela Valencia",
      "product": "Bronchicine CAe",
      "date": "2020-06-20",
      "next_vaccine_date": "2021-03-21"
    }
  ],
  "dewormings": [
    {
      "product": "Endogard",
      "weight": "1",
      "date": "2019-12-15"
    },
    {
      "product": "Endogard",
      "weight": "2.8",
      "date": "2020-01-18"
    },
    {
      "product": "Endogard",
      "weight": "2.7",
      "date": "2020-02-22"
    },
    {
      "product": "Ovistop",
      "weight": "4.2",
      "date": "2020-03-21"
    },
    {
      "product": "Ovistop",
      "weight": "6.2",
      "date": "2020-05-09"
    }
  ]
}
```
