import csv
import matplotlib.pyplot as plt

with open('C:\ProfGitHub\BAC-Advanced-Question\yelp.csv', 'r', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)

    header = 1

    xCoords = []
    yCoords = []
    cuisine = []
    chinese = []
    score = []
    grade = []
    rating = []
    reviews = []
    price = []
    xChinese = []
    yChinese = []

    for row in reader:
        if header == 1:
            header = 0
        else:
            xCoords.append(float(row[15]))
            yCoords.append(float(row[16]))
            cuisine.append(row[7])
            if(row[11]=="PEND"):
                score.append(15)
            elif int(float(row[11]))<0 :
                score.append(0)
            else:
                score.append(min(int(float(row[11])),30))
            grade.append(row[12])
            rating.append(float(row[21]))
            reviews.append(int(row[22]))
            price.append(len(row[20]))
            if row[7] == 'Chinese':
                chinese.append(1)
                xChinese.append(float(row[15]))
                yChinese.append(float(row[16]))
            else:
                chinese.append(0)

plt.grid()

#map the restaurants in Manhattan by chinese or non chinese

plt.plot(xCoords, yCoords, 'bs', xChinese, yChinese, 'bs')
plt.title('Chinese (blue) vs non-Chinese restaurants (gray)')
plt.show()

#map the restaurants in Manhattan by number of reviews

plt.scatter(xCoords, yCoords, s=20, c=reviews, cmap='Blues')
plt.title("Restaurants by number of reviews (Darker=more)")
plt.show()

#map the restaurants in Manhattan by rating

plt.scatter(xCoords, yCoords, s=20, c=rating, cmap='Blues')
plt.title("Restaurants by rating (Darker=higher)")
plt.show()

#map the restaurants over 4 stars and under 2.5 stars by reviews

good = []
gx = []
gy = []
bad = []
bx = []
by = []

for i in range(len(rating)) :
    if(rating[i]>=4) :
        good.append(reviews[i])
        gx.append(xCoords[i])
        gy.append(yCoords[i])
    elif(rating[i]<=3) :
        bad.append(reviews[i])
        bx.append(xCoords[i])
        by.append(yCoords[i])

plt.scatter(gx, gy, s=20, c=good, cmap='Blues')
plt.title("Restaurants 4 stars or above by number of ratings")
plt.show()

plt.scatter(bx, by, s=20, c=bad, cmap='Blues')
plt.title("Restaurants 3 stars or below by number of ratings")
plt.show()

#map the restaurants with more than 250 reviews by rating

rat = []
rx = []
ry = []

for i in range(len(reviews)):
    if reviews[i] >= 250 :
        rat.append(rating[i])
        rx.append(xCoords[i])
        ry.append(yCoords[i])

plt.scatter(rx, ry, s=20, c=rat, cmap='Blues')
plt.title("Restaurants with over 250 reviews by rating (darker = better)")
plt.show()

#map the restaurants in Manhattan by price

plt.scatter(xCoords, yCoords, s=20, c=price, cmap='Blues')
plt.title("Restaurants by price (Darker=higher)")
plt.show()

#map the restaurants in Manhattan by inspection score

plt.scatter(xCoords, yCoords, s=20, c=score, cmap='Blues')
plt.title("Restaurants by inspection score (Darker=worse)")
plt.show()

#Calculate and plot the average number of reviews for a restaurant vs the inspection score

rvs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rvsn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(score)):
    rvs[score[i]] += reviews[i]
    rvsn[score[i]] += 1.0

for i in range(len(rvs)):
    rvs[i] = rvs[i] / (rvsn[i]+1)

plt.plot(rvs)
plt.title("average number of reviews (y) vs inspection rating (x)")
plt.show()

#review cutoffs, dissatisfied or satisfied