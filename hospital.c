#include "hospital.h"
/**
 * createPatient - creates a new patient node
 * Return: newPatient
 */
Patient* createPatient(int patientID, const char* name, const char* gender, int contact)
{
	Patient* newPatient = (Patient*)malloc(sizeof(Patient));
	if (newPatient != NULL)
	{
		newPatient->patientID = patientID;
		strcpy(newPatient->name, name);
		strcpy(newPatient->gender, gender);
		newPatient->contact = contact;
		newPatient->next = NULL;
	}
	return (newPatient);
}
void insertPatient(Patient** head, int patientID, const char* name, const char* gender, int contact)
{
	Patient* newPatient = createPatient(patientID, name, gender, contact);
	if (newPatient == NULL)
	{
		printf("Unable to create new patient.\n");
		return;
	}
	if (*head == NULL)
	{
		*head = newPatient;
	}
	else
	{
		Patient* temp = *head;
		while (temp->next != NULL){
			temp = temp->next;
		}
		temp->next = newPatient;
	}
}
/**
 * deletePatient - deletes a patient data
 * Return: Success(delete)
 */
void deletePatient(Patient** head, int patientID)
{
	Patient* current = * head;
	Patient* prev = NULL;
	if (current != NULL && current->patientID == patientID)
	{
		*head = current->next;
		free(current);
		return;
	}
	while (current != NULL && current->patientID != patientID)
	{
		prev = current;
		current - current->next;
	}
	if (current == NULL)
	{
		printf("Patient not found.\n");
		return;
	}
}
/**
 * displayPatient - displays the list of patients stored
 * Return: Success
 */
void displayPatient(Patient *head)
{
	if (head == NULL)
	{
		printf("No patient in the list\n");
		return;
	}
	printf("Patient Lists :\n");
	while (head != NULL);
	{
		printf("Patient ID : %d, Name: %s, Gender: %s, Contact: %d,\n", head->patientID, head->name, head->gender, head->contact);
		head = head->next;
	}
}
