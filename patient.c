#include "hospital.h"
void username(char *firstname, char *lastname)
{
	printf("\033[1mFirst Name: \033[0m");
	fgets(firstname, sizeof(firstname), stdin);
	firstname[strcspn(firstname, "\n")] = '\0';

	printf("\003[1mLast Name: \033[0m");
	fgets(lastname, sizeof(lastname), stdin);
	lastname[strcspn(lastname, "\n")] = '\0';
}
void birthdate(char *day, char *month, char *year)
{
	while (1)
	{
		printf("\033[1mDay: \033[0m");
		scanf("%s", day);
		if (atoi(day) < 1 || atoi(day) > 31)
		{
			fprintf(stderr, "Invalid day!\n");
			continue;
		}
		else
		{
			*day = atoi(day);
			break;
		}
	}
	while (1)
	{
		printf("\033[1mMonth: \033[0m");
		scanf("%s", month);
		if (atoi(month) < 1 || atoi(month) > 12)
		{
			fprintf(stderr, "Invalid month!\n");
			continue;
		}
		else
		{
			*month = atoi(month);
		}
		break;
	}
	while (1)
	{
		printf("\n\033[1mYear: \033[0m");
		scanf("%s", year);
		if (atoi(year) < 1930 || atoi(year) > 2050)
		{
			fprintf(stderr, "Invalid Year!\n");
			continue;
		}
		else
		{
			*year = atoi(year);
		}
		break;
	}
}
void genderchoice(char *gender)
{
	int choice;

	printf("\033[1mPlease choose your gender: \033[0m");
	printf("1) Male\n");
	printf("2) Female\n");
	printf("ENTER CHOISE\n");
	scanf("%d", &choice);

	if (choice == 1)
	{
		printf("Male");
	}
	else if (choice == 2)
	{
		printf("Female");
	}
	else
	{
		printf("Invalid Choice");
	}
}
