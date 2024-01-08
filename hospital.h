#ifndef _MAIN_H_
#define _MAIN_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Patient
{
	int patientID;
	char name[50];
	char gender[50];
	int contact;
	struct Patient *next;
}Patient;

Patient* createPatient(int patientID, const char* name, const char* gender, int contact);
void insertPatient(Patient** head, int patientID, const char* name, const char* gender, int contact);
void deletePatient(Patient** head, int patientID);
void displayPatient(Patient* head);
void freePatient(Patient** head);
void username(char *firstname, char *lastname);
void genderchoice(char* gender);
void askcontact(int *phone, char *email);
void birthdate(char *day, char *month, char *year);

#endif  /*MAIN_H*/
