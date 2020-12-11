import mysql.connector as mysql


def dataupdate(student_group, input_activity, input_outside, input_workingtime, input_environment, input_company,
               input_skills,
               input_personally, input_problems_dealing, input_public, min_salary, wish_salary
               ):
    mydb = mysql.connect(host="localhost",
                         user="root",
                         passwd="chatbot2020",
                         database="chatbot",
                         )
    activity = ""
    outside = ""
    workingtime = ""
    environment = ""
    company = ""
    skills = ""
    personally = ""
    problems_dealing = ""
    public = ""

    if int(input_activity) > 2:
        activity += "Abwechslungsreiche Tätigkeit, Herausfordernde Tätigkeit, Aufstiegsmöglichkeiten, " \
                    "Weiterbildungsmöglichkeiten "
    else:
        activity += "NA"
    if int(input_outside) > 2:
        outside += "Kundenkontakt,Dienstreisen, Gute Beziehung zu Vorgesetzten"
    else:
        outside += "NA"
    if int(input_workingtime) > 2:
        workingtime += "Flexible Arbeitszeit, Überstundenkonto, Arbeitszeiterfassung"
    else:
        workingtime += "NA"

    if int(input_environment) > 2:
        environment += "Lockere Arbeitsatmosphäre, Anbindung an öffentliche Verkehrsmittel, Kantine, moderne Büro"
    else:
        environment += "NA"

    if int(input_company) > 2:
        company += "Innovatives Unternehmen, Etabliertes Unternehmen, Start-up"
    else:
        company += "NA"

    if int(input_skills) > 2:
        skills += "Kommunikationsfähigkeit, Organisationsfähigkeit und Teamfähigkeit"
    else:
        skills += "NA"

    if int(input_personally) > 2:
        personally += "Lernbereitschaft, Neugier, Selbstdisziplin und analytisches Denkenvermögen"
    else:
        personally += "NA"

    if int(input_problems_dealing) > 2:
        problems_dealing += "Problemlösungskompetenz, Kritikfähigkeit, Stressresistenz"
    else:
        problems_dealing += "NA"

    if int(input_public) > 2:
        public += "Integrationsbereitschaft, Präsentationsskills und Empathie"
    else:
        public += "NA"

    mycursor = mydb.cursor()
    # sql = "CREATE TABLE userinput2 (activity LONGTEXT,outside LONGTEXT,workingtime LONGTEXT,environment " \
    #       "LONGTEXT,company LONGTEXT,skills LONGTEXT,personally LONGTEXT,problems_dealing VARCHAR(" \
    #       "255),public LONGTEXT,min_salary VARCHAR(255),wish_salary VARCHAR(255)); "

    # sql = "CREATE TABLE userinput(student_group VARCHAR(255), activity LONGTEXT, outside LONGTEXT, workingtime
    # LONGTEXT, environment LONGTEXT, company LONGTEXT, skills LONGTEXT, personally LONGTEXT, problems_dealing
    # VARCHAR(255), public LONGTEXT, min_salary VARCHAR(255), wish_salary VARCHAR(255)); "

    sql = 'INSERT INTO userinput (student_group, activity, outside, workingtime, environment, company, skills, ' \
          'personally,problems_dealing, public, min_salary, wish_salary) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}",' \
          '"{6}","{7}","{8}","{9}","{10}","{11}");'.format(
        student_group, activity, outside, workingtime, environment, company, skills, personally, problems_dealing,
        public, min_salary, wish_salary)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "user input inserted!")
