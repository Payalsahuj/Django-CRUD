from django.shortcuts import render, redirect
import json

data_file_path = 'db.json'  # Path to the JSON data file

# Create view function
def create(request):
    if request.method == 'POST':
        # Retrieve the data from the form
        name = request.POST['name']
        age = request.POST['age']
        city = request.POST['city']
        
        # Read existing data from the JSON file
        with open(data_file_path, 'r') as f:
            data = json.load(f)
        
        # Append a new entry to the data list
        data.append({'name': name, 'age': age, 'city': city})
        
        # Write the updated data back to the JSON file
        with open(data_file_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        return redirect('read')  # Redirect to the read route

    return render(request, 'create.html')


# Read view function

def read(request):
    with open(data_file_path, 'r') as f:
        data = json.load(f)

    return render(request, 'read.html', {'data': data})

# Update view function
def update(request):
    if request.method == 'POST':
        # Retrieve the updated data from the form
        updated_name = request.POST['name']
        updated_age = request.POST['age']
        updated_city = request.POST['city']
        index = int(request.POST['index'])  # Retrieve the index of the entry to update
        
        # Read existing data from the JSON file
        with open(data_file_path, 'r') as f:
            data = json.load(f)
        
        # Update the data entry at the specified index
        if 0 <= index < len(data):
            data[index]['name'] = updated_name
            data[index]['age'] = updated_age
            data[index]['city'] = updated_city
            
            # Write the updated data back to the JSON file
            with open(data_file_path, 'w') as f:
                json.dump(data, f, indent=4)
        
        return redirect('read')  # Redirect to the read route

    with open(data_file_path, 'r') as f:
        data = json.load(f)
    
    return render(request, 'update.html', {'data': data})



# Delete view function

def delete(request):
    if request.method == 'POST':
        index = int(request.POST['index'])  # Retrieve the index of the entry to delete
        
        # Read existing data from the JSON file
        with open(data_file_path, 'r') as f:
            data = json.load(f)
        
        # Remove the data entry at the specified index
        if 0 <= index < len(data):
            del data[index]
            
            # Write the updated data back to the JSON file
            with open(data_file_path, 'w') as f:
                json.dump(data, f, indent=4)
        
        return redirect('read')  # Redirect to the read route

    with open(data_file_path, 'r') as f:
        data = json.load(f)
    
    return render(request, 'delete.html', {'data': data})