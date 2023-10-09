# import packages
import psutil
import time
from sqlalchemy.orm import sessionmaker
from database import engine,Ram_data

# some nesseccery configs
Session = sessionmaker(bind=engine)
session = Session()



# get ram usage history
def get_memory_info():
    memory = psutil.virtual_memory()
    total_mem_mb = memory.total // (1024 * 1024)  # Convert bytes to megabytes
    free_mem_mb = memory.free // (1024 * 1024)  # Convert bytes to megabytes
    used_mem_mb = memory.used // (1024 * 1024)  # Convert bytes to megabytes

    return {
        'total': total_mem_mb,
        'free': free_mem_mb,
        'used': used_mem_mb
    }


while True:
    # Get memory information
    memory_info = get_memory_info()

    # Print the results
    print(f"Total Memory: {memory_info['total']} MB")
    print(f"Free Memory: {memory_info['free']} MB")
    print(f"Used Memory: {memory_info['used']} MB")
    data=Ram_data(total=memory_info['total'],available=memory_info['free'],
             used=memory_info['used'])
    session.add(data)
    session.commit()

    # Wait for 60 seconds
    time.sleep(60)