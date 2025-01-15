import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots() #создаем область для рисунка и оси
ax.plot(x, y) #Добавляем данные на график
plt.show()


x = np.random.uniform (0, 1, 1000)
y = np.random.uniform (0, 1, 1000)
ax.scatter(x,y)


x = np.arange (10)
y = np.random.uniform (0, 1, 10)
ax.bar(x,y)


z = np.random.uniform (0, 1, (8,8))
ax.imshow(z)


z = np.random.uniform (0, 1, (8,8))
ax.contourf(z)


z = np.random.uniform (0, 1, 5)
label = ['Subaru', 'Honda', 'Toyota', 'Suzuki', 'Mitsubishi']
exp = [0.07, 0.02, 0, 0, 0.01]
fig, (ax) = plt.subplots()
plt.title('Ваша марка машины?', fontsize=16)
ax.pie(z, labels=label, explode=exp)



x = np.arange (10)
y = np.random.uniform (0, 1, 10)
ax.plot(x,y, color = 'green')
ax.bar(x,y)


x=np.linspace(0, 10, 100)
y1, y2 = np.sin(x), np.cos(x)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('Sin wave')
ax2.set_title('Cos wave')
ax1.plot(x, y1, color='C1', label='Sin', lw=5, linestyle='--')
ax2.plot(x, y2, color='C0', label='Cos', lw=2, marker='.')


f = plt.figure(figsize=(15, 10))
ax_3d = f.add_subplot(projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(50 * z)
y = z * np.cos(50 * z)
ax_3d.scatter(x, y, z, color='red', alpha=1)
ax_3d.set_xlabel('x', size='15')
ax_3d.set_ylabel('y', size='15')
ax_3d.set_zlabel('z', size='15')
