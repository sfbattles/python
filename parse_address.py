import usaddress


def tag_address(address):
    try:
        parsed_address = usaddress.tag(address.lower())
        return parsed_address
    except usaddress.RepeatedLabelError:
        return []


def write_line(currentline):
    with open("parcedhomeincidentalbusiness.csv", "a+") as result_file_handle:
        result_file_handle.write(currentline)


f = open("parcedhomeincidentalbusiness.csv", "w")
f.close()

with open("homeincidentalbusiness.csv", "r") as file_handle:
    for loop, line in enumerate(file_handle):
        if loop == 0:
            write_line(line)
        else:
            line.rstrip()
            contents = line.split("|")
            street_address = ""
            city = ""
            state = ""
            zipcode = ""
            result = tag_address(contents[8])
            try:
                if "AddressNumber" in result[0].keys():
                    street_address += result[0]["AddressNumber"] + " "
                if "StreetName" in result[0].keys():
                    street_address += result[0]["StreetName"] + " "
                if "StreetNamePreType" in result[0].keys():
                    street_address += result[0]["StreetNamePreType"] + " "
                if "StreetNamePostType" in result[0].keys():
                    street_address += result[0]["StreetNamePostType"] + " "
                if "OccupancyType" in result[0].keys():
                    street_address += result[0]["OccupancyType"] + " "
                if "OccupancyIdentifier" in result[0].keys():
                    street_address += result[0]["OccupancyIdentifier"] + " "
                if "StreetNamePreDirectional" in result[0].keys():
                    street_address += result[0]["StreetNamePreDirectional"] + " "
                if "AddressNumberSuffix" in result[0].keys():
                    street_address += result[0]["AddressNumberSuffix"] + " "
                if "PlaceName" in result[0].keys():
                    city += result[0]["PlaceName"] + " "
                if "StateName" in result[0].keys():
                    state += result[0]["StateName"] + " "
                if "ZipCode" in result[0].keys():
                    zipcode += result[0]["ZipCode"] + " "
            except IndexError:
                street_address = "Address Not Entered"

            print(street_address)
            print(result)
            contents[3] = street_address
            contents[4] = city  # city
            contents[8] = state  # state
            contents[12] = zipcode  # zip
            thestr = "|".join(contents)
            write_line(thestr)
