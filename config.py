
from secrets import username, password

# rds_connection_string = f"{username}:{password}@localhost:5432/etl_team5"
# engine = create_engine(f'postgresql://{rds_connection_string}')

database = "postgres"
# database = "heroku"

connect_string = ""

if database == "postgres":
    # connect_string = "postgresql://username:password@localhost:5432/etl_team5"

    connect_string = f"postgresql://{username}:{password}@localhost:5432/etl_team5"
    
elif database == "heroku":        
    #connect_string = f"postgresql://b0062c13dd9bc03400c5db309c3dbca1d5d21f486adc48b7c5412f9a8e456@ec2-54-235-108-217.compute-1.amazonaws.com:5432/d5tufocs1d1pci"
    connect_string = f"postgres://uothqbtdpaanvg:2fde20bbd35347df59d70e1177499cff2eb72b2629941b7c82a071fe36677ec0@ec2-100-24-139-146.compute-1.amazonaws.com:5432/d6rafo5fo1kucb"

from secrets import username, password

# rds_connection_string = f"{username}:{password}@localhost:5432/etl_team5"
# engine = create_engine(f'postgresql://{rds_connection_string}')

# database = "postgres"

database = "heroku"

connect_string = ""

if database == "postgres":
    # connect_string = "postgresql://username:password@localhost:5432/etl_team5"

    connect_string = f"postgres://{username}:{password}@localhost:5432/etl_team5"
    
elif database == "heroku":        
    connect_string = "postgres://uothqbtdpaanvg:2fde20bbd35347df59d70e1177499cff2eb72b2629941b7c82a071fe36677ec0@ec2-100-24-139-146.compute-1.amazonaws.com:5432/d6rafo5fo1kucb"

