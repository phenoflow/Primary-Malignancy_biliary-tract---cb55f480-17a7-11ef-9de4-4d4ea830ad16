# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"89593.0","system":"readv2"},{"code":"41313.0","system":"readv2"},{"code":"65124.0","system":"readv2"},{"code":"61643.0","system":"readv2"},{"code":"52537.0","system":"readv2"},{"code":"72445.0","system":"readv2"},{"code":"8711.0","system":"readv2"},{"code":"23433.0","system":"readv2"},{"code":"35039.0","system":"readv2"},{"code":"10949.0","system":"readv2"},{"code":"16915.0","system":"readv2"},{"code":"105613.0","system":"readv2"},{"code":"36495.0","system":"readv2"},{"code":"107299.0","system":"readv2"},{"code":"40438.0","system":"readv2"},{"code":"7982.0","system":"readv2"},{"code":"58088.0","system":"readv2"},{"code":"74896.0","system":"readv2"},{"code":"110147.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_biliary-tract-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["biliary---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["biliary---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["biliary---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
