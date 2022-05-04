# Pet Care API
API Demo created with [FastAPI](https://fastapi.tiangolo.com/) + [CosmosDB](https://azure.microsoft.com/es-es/free/cosmos-db/)

## Virtual environment (Local Development)

### Install virtual environment
```
pip install virtualenv
```
### Create virtual environment
```bash
# OSX / Linux(Bash)
virtualenv <folder_name>

# Windows
python -m venv <folder_name>
```

### Activate virtual environment

```bash
# OSX / Linux(Bash)
<folder_name>/bin/activate

# CMD
<folder_name>\Scripts\Activate.bat

# Powershell
<folder_name>\Scripts\Activate.ps1

# Bash Shell
. ./<folder_name>/Scripts/activate
```

### Deactivate virtual environment
```
deactivate
```

### Create environment variables
```bash
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
```

### Run locally
```bash
# Download dependencies
pip install --no-cache-dir --upgrade -r requirements.txt
# Run servers
uvicorn app.main:app --port 8000 --reload
```

### Run as Docker container
```bash
docker build -t pet-care:1.0 .

# Use your cosmos account values
docker run --name pet-care -p 8000:8000 -e COSMOS_URI="YOUR_URI" -e COSMOS_KEY="YOUR_KEY" -e COSMOS_DB="YOUR_DB" -e COSMOS_CONTAINER="YOUR_CONTAINER" <image_name>:<tag>
```

### Run on Kubernetes cluster
```bash
# Execute the docker build & push
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