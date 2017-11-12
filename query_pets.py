import sqlite3
import sys

def query_pets():
    try:
        con = sqlite3.connect('pets.db')

        while True:
            person_id = raw_input('Enter and ID number of desired person: ')
            if person_id == '-1':
                sys.exit()
            else:
                try:
                    person_id = int(person_id)
                except:
                    print 'Person not found, please try differnt ID'
                    continue
            c = con.cursor()
            c.execute('SELECT * FROM person WHERE id = ?', [(person_id)])
            row_data = c.fetchone()

            if row_data == None:
                print 'Invalid ID number, try differnt ID'
                continue

            print '{} {} is {} yrs old.'.format(row_data[1], row_data[2], row_data[3])

            c.execute('''SELECT person.first_name, person.last_name, pet.name,
                        pet.breed, pet.age, pet.dead
                        FROM pet
                        LEFT JOIN person_pet
                        ON pet.id = person_pet.pet_id
                        LEFT JOIN person
                        ON person_pet.person_id = person.id
                        WHERE person.id = ?''',[(person_id)])
            pet_data = c.fetchall()

            for pet in pet_data:
                pet_name = pet[2]
                pet_breed = pet[3]
                pet_age = pet[4]
                pet_dead = pet[5]
                if pet_dead == 1:
                    print '{} {} owned {}, a {}, that was died in {} yrs old'. \
                        format(row_data[1], row_data[2], pet_name, pet_breed, pet_age)
                elif pet_dead == 0:
                    print '{} {} owns {}, a {}, which is {} yrs old'.\
                        format(row_data[1], row_data[2], pet_name,pet_breed, pet_age)

            # print pet_data

    except sqlite3.Error,e:
        print 'Error: %s' %e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()

if __name__ == "__main__":
    query_pets()