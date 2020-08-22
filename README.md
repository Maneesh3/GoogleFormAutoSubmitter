# GoogleFormAutoSubmitter
Google form response auto submitter using python

> DISCLAIMER: This project/code is done as an example, ONLY works for forms without sign-In

## Instructions:
Skip to Useage section if you are here for code and process, else keep reading
- A sample Google form is created **see pdf file** `SURVEY.pdf`, I removed the form now. so, dont get too excited to send responses to me.
- The program is written based on the form, so feel free to edit to your convinience.
- To fill the data, we can do random..., but whats the fun right?!
- so here are come conditions i considered:
```
name = random names
age =  [16 .. 23] -> 50% of 18,19 years
1) How often did you communicate with friends and family by
phone, text, app,or using the Internet?
    Basically every day -> 70%
    A few times a month -> 25%
    Not at all          -> 5%
2) Did you do any work for income ?
    Yes -> AGE [19-23] 75% Yes, 25% No
    No  AGE < 18
3) Would you say your health in general is good, fair, or poor?
    Good    60%     AGE<18 100%
    Fair    35%     AGE [19-23] 80% Fair, 10% good, 10% poor
    Poor    5%
4) How did covid 19 affect you financially?
    Completely      70%
    Partially       23%
    Not at all      7%
5) Did covid 19 help you to be more clean and sanitized?
    Yes     70%
    No      30%
```
- these percentages is like probability to choose that option

**OK OK OK, how to use?-->**
## Useage:
*Steps:*
1. Open Network tab via Inspect Element
2. Send a sample response to hte form u selected
3. We can see this Network tab refreshes, observe the first POST request
4. From this request, we can get this form's `event.<id>` values
5. Based on these values modify your code accordingly with the help of file `form.py`
6. Replace the `_FORM_LINK` variable to ur own
7. Lastly if you are doing something like *attacking on that Google Form*, I am not responsible, also use a VPN da..

- `random.choices` - used to get random weighted values (read documentation, dont be lazy)
- `requests.post` - send `POST` request
