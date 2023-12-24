import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


csv_file_path = 'laptops_0-1499.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)


# Check for CPU mistake
CPU_list = []
for i in range(1500):
    cpu_name = df["CPU"][i]
    CPU_list.append(cpu_name)

# Distribution graph of name length
CPU_name_length = []
for i in range (1500):
    if isinstance(CPU_list[i],str):
        CPU_name_length.append(len(CPU_list[i]))
    else:
        CPU_name_length.append(0)

CPU_Error_ID_list = []
for i in range(1500):
    if CPU_name_length[i] >= 80 or CPU_name_length[i] <= 3:
        CPU_Error_ID_list.append(i)

print(CPU_Error_ID_list)
print(len(CPU_Error_ID_list))
for i in range(5):
    print(CPU_Error_ID_list[i], CPU_list[CPU_Error_ID_list[i]])
# Plot histogram
plt.hist(CPU_name_length, bins =600,  edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of CPU name')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Check Resolution Mistake
Res_list = []
for i in range(1500):
    res_name = df["Resolution"][i]
    Res_list.append(res_name)

# Distribution graph of name length
Res_name_length = []
for i in range (1500):
    if isinstance(Res_list[i],str):
        Res_name_length.append(len(Res_list[i]))
    else:
        Res_name_length.append(0)

Res_Error_ID_list = []
for i in range(1500):
    if Res_name_length[i] >= 80 or Res_name_length[i] <= 3:
        Res_Error_ID_list.append(i)

print(Res_Error_ID_list)
print(len(Res_Error_ID_list))

# Plot histogram
plt.hist(Res_Error_ID_list, bins =600,  edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of Res name')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# Check for GPU mistake
GPU_list = []
for i in range(1500):
    gpu_name = df["GPU"][i]
    GPU_list.append(gpu_name)

# Distribution graph of name length
GPU_name_length = []
for i in range (1500):
    if isinstance(GPU_list[i],str):
        GPU_name_length.append(len(GPU_list[i]))
    else:
        GPU_name_length.append(0)

GPU_Error_ID_list = []
for i in range(1500):
    if GPU_name_length[i] >= 80 or GPU_name_length[i] <= 3:
        GPU_Error_ID_list.append(i)

print(GPU_Error_ID_list)
print(len(GPU_Error_ID_list))

# Plot histogram
plt.hist(GPU_name_length, bins =600,  edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of GPU name')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


#Check for RAM Error
RAM_list = []
for i in range(1500):
    ram_value = df["RAM"][i]
    RAM_list.append(ram_value)

# Distribution graph of value length
RAM_value_length = []
for i in range(1500):
    if isinstance(RAM_list[i], str):
        RAM_value_length.append(len(RAM_list[i]))
    else:
        RAM_value_length.append(0)

RAM_Error_ID_list = []
for i in range(1500):
    if RAM_value_length[i] >= 80 or RAM_value_length[i] <= 0:
        RAM_Error_ID_list.append(i)

print(RAM_Error_ID_list)
print(len(RAM_Error_ID_list))

# Plot histogram
plt.hist(RAM_value_length, bins=600, edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of RAM Value')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# Check Monitor mistake
Monitor_list = []
for i in range(1500):
    monitor_value = df["Monitor"][i]
    Monitor_list.append(monitor_value)

# Distribution graph of value length
Monitor_value_length = []
for i in range(1500):
    if isinstance(Monitor_list[i], str):
        Monitor_value_length.append(len(Monitor_list[i]))
    else:
        Monitor_value_length.append(0)

Monitor_Error_ID_list = []
for i in range(1500):
    if Monitor_value_length[i] >= 80 or Monitor_value_length[i] <= 3:
        Monitor_Error_ID_list.append(i)

print(Monitor_Error_ID_list)
print(len(Monitor_Error_ID_list))

# Plot histogram
plt.hist(Monitor_value_length, bins=600, edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of Monitor Value')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


#Check Storage
Storage_list = []
for i in range(1500):
    storage_value = df["Storage"][i]
    Storage_list.append(storage_value)

# Distribution graph of value length
Storage_value_length = []
for i in range(1500):
    if isinstance(Storage_list[i], str):
        Storage_value_length.append(len(Storage_list[i]))
    else:
        Storage_value_length.append(0)

Storage_Error_ID_list = []
for i in range(1500):
    if Storage_value_length[i] >= 80 or Storage_value_length[i] <= 3:
        Storage_Error_ID_list.append(i)

print(Storage_Error_ID_list)
print(len(Storage_Error_ID_list))

# Plot histogram
plt.hist(Storage_value_length, bins=600, edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of Storage Value')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#Check OS
OS_list = []
for i in range(1500):
    os_value = df["OS"][i]
    OS_list.append(os_value)

# Distribution graph of value length
OS_value_length = []
for i in range(1500):
    if isinstance(OS_list[i], str):
        OS_value_length.append(len(OS_list[i]))
    else:
        OS_value_length.append(0)

OS_Error_ID_list = []
for i in range(1500):
    if OS_value_length[i] >= 80 or OS_value_length[i] <= 3:
        OS_Error_ID_list.append(i)

print(OS_Error_ID_list)
print(len(OS_Error_ID_list))

# Plot histogram
plt.hist(OS_value_length, bins=600, edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of OS Value')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


## Check Weight mistake
# Weight_list = []
# for i in range(1500):
#     weight_value = df["Weight"][i]
#     Weight_list.append(weight_value)
#
# # Distribution graph of value length
# Weight_value_length = []
# for i in range(1500):
#     if isinstance(Weight_list[i], str):
#         Weight_value_length.append(len(Weight_list[i]))
#     else:
#         Weight_value_length.append(0)
#
# Weight_Error_ID_list = []
# for i in range(1500):
#     if Weight_value_length[i] >= 80 or Weight_value_length[i] <= 3:
#         Weight_Error_ID_list.append(i)
#
# print(Weight_Error_ID_list)
# print(len(Weight_Error_ID_list))
#
# # Plot histogram
# plt.hist(Weight_value_length, bins=600, edgecolor='black')  # Adjust the number of bins as needed
# plt.title('Length of Weight Value')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()

Price_list = []
for i in range(1500):
    price_value = df["Price"][i]
    Price_list.append(price_value)

# Distribution graph of value length
Price_value_length = []
for i in range(1500):
    if isinstance(Price_list[i], (int, float)):
        Price_value_length.append(len(str(Price_list[i])))
    else:
        Price_value_length.append(0)

Price_Error_ID_list = []
for i in range(1500):
    if Price_value_length[i] >= 80 or Price_value_length[i] <= 2:
        Price_Error_ID_list.append(i)

print(Price_Error_ID_list)
print(len(Price_Error_ID_list))

# Plot histogram
plt.hist(Price_value_length, bins=600, edgecolor='black')  # Adjust the number of bins as needed
plt.title('Length of Price Value')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()



combined_list = list(set(CPU_Error_ID_list + GPU_Error_ID_list + Res_Error_ID_list + RAM_Error_ID_list + Monitor_Error_ID_list + OS_Error_ID_list + Price_Error_ID_list))

print(combined_list)
print(len(combined_list))

# Create a new DataFrame with rows not in combined_list
filtered_df = df.loc[~df.index.isin(combined_list)]

# Specify the path for the new CSV file
new_csv_file_path = 'filtered_laptops_1.csv'

# Write the filtered DataFrame to a new CSV file
filtered_df.to_csv(new_csv_file_path, index=False)

print(f"Filtered data saved to {new_csv_file_path}")
