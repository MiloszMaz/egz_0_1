import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from var_dump import var_dump


# Odwzoruj wykres znajdujący się w pliku o nazwie w1.png. Odcienie kolorów mogą się różnić, jednak
# główne barwy muszą być zachowane. Zapisz wykres w formacie jpg za pomocą kodu.
def zadanie1():
    print('Zadanie 1')

    fig, ax = plt.subplots()

    ax2 = ax.twinx()

    plt.ylim([-1.0, 1])
    plt.xlim([0, 5])

    plt.yticks(np.arange(-1.0, 1, 0.5))

    # 1 linia
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    ax.plot(x, y, linewidth=1.5, color='orange', markersize=3, linestyle='dotted', label='sin(x)')

    # 2 linia
    x = np.linspace(0, 2 * np.pi, 100)
    z = np.cos(x) / 2
    ax2.plot(x, z, linewidth=1.5, color='brown', markersize=3, linestyle='dotted', label='cos(x)')

    # Legenda
    ax.set_title('To jest tytuł wykresu')
    ax.set_ylabel('oś lewa')
    plt.xlabel("oś dolna")

    #ax.yaxis.set_tick_params(which='both', right=True, labelright=True, left=True, labelleft=True)

    #ax2.yaxis.set_tick_params(which='both', right=False, labelright=False, left=False, labelleft=False)
    ax2.set_ylabel('oś prawa')

    ax2.legend(loc='lower center')
    ax.legend(loc='center right')

    # Zapis
    #plt.savefig("dane.jpg")

    plt.show()

# Zad.2. W jednym pliku wykonaj poniższe czynności:
# • załaduj dane z pliku ceny1.xlsx jako ramkę danych (Data Frame),
# • stwórz wykres liniowy prezentujący dane zawarte w ramce danych
# • umieść swój numer indeksu w lewym górnym rogu wykresu.
# Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
# Zapisz wykres w formacie png za pomocą kodu.
def zadanie2():
    print('Zadanie 2')

    xlsx = pd.ExcelFile('ceny1.xlsx')
    df = pd.read_excel(xlsx, index_col=0)

    # grupowanie

    grouped_df = df.groupby("Rodzaje towarów")

    grouped_lists_wartosc = grouped_df["Wartość"].apply(list)
    grouped_lists_rok = grouped_df["Rok"].apply(list)

    grouped_lists_wartosc = grouped_lists_wartosc.reset_index()
    grouped_lists_rok = grouped_lists_rok.reset_index()

    #print(grouped_lists_wartosc['Wartość'][1])
    #print(grouped_lists_rok)

    # tworzenie linii

    fig = plt.figure()

    myaxes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    myaxes.set_title('Wykres wzrostu cen produktów')
    myaxes.set_xlabel('Rok')
    myaxes.set_ylabel('Wartość')

    plt.ylim([0, 8])

    # 1 linia - ryz
    myaxes.plot(grouped_lists_rok['Rok'][1], grouped_lists_wartosc['Wartość'][1], 'r', label='ryż - za 1kg')

    # 2 linia - maka
    myaxes.plot(grouped_lists_rok['Rok'][0], grouped_lists_wartosc['Wartość'][0], 'g', label='mąka pszenna - za 1kg')

    # legenda
    myaxes.legend(loc='upper left')

    plt.savefig("zadanie2.png")

    plt.show()


def zadanie3():
    print('Zadanie 3')

    df = pd.read_csv('nieruchomosci1.csv', header=None, sep=";", decimal=".")

    df_1 = df.T

    #print(df_1)

    grouped_df = df_1.groupby(0)
    grouped_list_label = grouped_df[1].apply(list)
    grouped_list_value = grouped_df[4].apply(list)

    grouped_list_label = grouped_list_label.reset_index()
    grouped_list_value = grouped_list_value.reset_index()

    #df_1.reset_index()

    grouped_label = grouped_list_label.T
    grouped_value = grouped_list_value.T

    grouped_label = grouped_label.reset_index()
    grouped_value = grouped_value.reset_index()

    grouped_value_pierwotny = []
    for one_value in grouped_value[0][1]:
        grouped_value_pierwotny.append(int(one_value.replace(" ", "")))


    grouped_pierwotny_label = grouped_label[0][1]

    print(grouped_value_pierwotny)
    print(grouped_pierwotny_label)

    df_new = pd.DataFrame(grouped_value_pierwotny, index=grouped_pierwotny_label)

    plot = df_new.plot.pie(subplots=True)

    #grupa = df_1.groupby([0])

    #df_1.plot(kind='pie', subplots=True)

    #for oneRow in df_1:
    #    print(oneRow)

    plt.show()

def cw1():
    df = pd.read_csv('dane_cwiczenia.csv', header=0, sep=";", decimal=".")

    grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':["sum"]})

    grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6,6), colors=['red', 'green'])

    plt.legend(loc='lower right')
    plt.title('Suma zamówienia dla sprzedawcy')
    plt.show()


if __name__ == '__main__':
    #zadanie1()

    #zadanie2()

    #cw1()

    zadanie3()

