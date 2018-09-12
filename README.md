# Playersprofile 
rest api for athletes player profiles data

## Starting an Project
- django-admin.py startproject myfirstproject
- creates your first project where you could host your DB, api projects, web proejcts, can all be hosted within this main project. 

### Starting an App inside of a project
- python manage.py startapp myfristappweb
- allows you to launch your specific web service for your program.

### Running your django server
``` python

python mange.py runserver

```

## Key Notes Thus Far
- endpoint is going to be hello-view, and it's going to render the as_view
- Updating Admin site is very crucial 
- adding mulitple projects is another key lesson learned.

### Models & Database Migrations 
- Database migrations can be updated 

### Point of Serilizers 
- Serializers allow you to create a post and put to your database 
- Allows you convert json data into python objects that can be stored in the database

### APIVIEWS (Custom API Logic)
- setup for loading logic 
- different then a view set because it is based on custom logic

### Viewsets (Low Customization API Logic)
- simple and quick for CRUD application
- viewset automagically saves the creates a template for your data page 
- Viewsets require you to go the specifc object in the data to do more specific commands such as update


### Login Authentication
- When working with Login profiles we noticed that there are key authorizaiton tokens that we have to be aware off 
- key learnings of adding authnetications and login information

### Basic Requirements 
- Create new profile 
    - validate profile data

- List Existing profiles
    - search for profiles

- View Player Dashboard
   - displays risk score
   - injury history
   - tib_anterior_lle
   - tib_anterior_rle

### Issues when the sensor collection architecture
- Currently struggling to figure out how to save the emg data from the different sessions that the athletes will have. Seeing that there is an option for one to many relations. Basic fundamental table for the sensor collection could be emg:float, timestamp:timestamp, user_profile:foreignkey

### Player Dashboard 

*** Definition ***

'Get /api/players/<id>'

***Response***

``` json

[
  {"id":01,
   "name":"Lebron James",
   "age":36,
   "profile_img":"www.bin.com/lebronjames",
   "injury_history":"Poor knees",
   "current_injury":"None available",
   "risk_score":3,
   "rightle":[
         {"tib_anterior":[{"max":50,"medium":60,"minimal":80}],
          "peroneals":[{"max":60,"medium":10,"minimal:30}],
          "med_gastro":[{"max":20,"medium":30,"minimal":50}],
          "lat_gastro":[{"max":30,"medium":50,"minimal":20}]
          }
            ],
   "leftle":[
          {"tib_anterior":[{"max":50,"medium":60,"minimal":80}],
          "peroneals":[{"max":60,"medium":10,"minimal:30}],
          "med_gastro":[{"max":20,"medium":30,"minimal":50}],
          "lat_gastro":[{"max":30,"medium":50,"minimal":20}],
          }
          ],
   "assessment":"Player is serious risk on injuring their tibular anterior",
   "treatment":"Soak and ice knee until, and go through plyo excersises"
   }]
   
  ```
  ### List all players
  
  *** Definition ***

'Get /api/players/'

### Definition
  
  ``` json 
  [
    {"id":01,
    "name":"Lebron James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
     {"id":02,
    "name":"Lebron James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
     {"id":03,
    "name":"Lebron James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
     {"id":04,
    "name":"Kyle James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
  ]
```
### Post players emg data 

*** Defintion ***

'Post /api/players/<id>'
  
### Definition

``` json
[
  {"name":"Kehlin Swain",
  "age":22,
  "profile_image":"www.hello.com/img",
  "tib_anterior_lle":[1,2,4,5,6,9],
  "tib_anterior_rle":[1,2,4,5,6,9],
  "peroneals_rle":[1,2,3,4,5,9],
  "peroneals_lle":[9,8,7,6,3],
  "med_gastro_rle":[8,9,0,1,7],
  "med_gastro_lle":[10,20,9,9,1],
  "lat_gastro_rle":[12,32,90,3,2],
  "lat_gastro_llt":[12,45,60,1,3],
  }
]
```

### Post players assessment data 

*** Defintion ***

'Post /assessment/<id>'
  
### Definition

``` json
[
  {"assessment":"Hello this is my assessment of how the athlete is doing in his trials"
   "treatment":"Your athlete will need to do x,y, and z to complete his next actions"
  }
]

# a-z_report_project
This will be a repo for the a-z report project
