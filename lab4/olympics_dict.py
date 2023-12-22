taekwondo_olympics2020_w49k = {
    "Gold": 'Thailand',
}

if __name__ == '__main__':
    taekwondo_olympics2020_w49k.update({
        "Silver": 'Spain',
        "Bronze": ['Israel', 'Serbia']
    })

    print("The list of medals in Taekwondo Olympics 2020 Women 49kg Kilogram:")
    for medal, country in taekwondo_olympics2020_w49k.items():
        if isinstance(country, list):
            for c in country:
                print(f"{medal} received {c} medal")
        else:
            print(f"{country} received {medal} medal")

    taekwondo_olympics2020_w49k.update({
        "Gold": {'Thailand'},
        "Silver": {'Spain'},
        "Bronze": {'Israel', 'Serbia'}
    })

    # Print the dictionary itself
    print(f"The dictionary of medals is: {taekwondo_olympics2020_w49k}")
