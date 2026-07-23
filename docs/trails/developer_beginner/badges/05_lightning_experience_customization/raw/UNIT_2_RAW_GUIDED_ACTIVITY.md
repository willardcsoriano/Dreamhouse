badge5unit2

https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_apps?trail_id=force_com_dev_beginner

Create and Customize Agentforce 360 Platform Apps

Learning Objectives

After completing this unit, you’ll be able to:

    Describe the benefits of Lightning apps.
    Create a Lightning app with custom branding.
    List two best practices for planning Lightning apps for your org.

Note
Accessibility

This unit requires some additional instructions for screen reader users. To access a detailed screen reader version of this unit, click the link below:

Open Trailhead screen reader instructions.
What Is a Lightning App?

An app is a collection of items that work together to serve a particular function. In Lightning Experience, Lightning apps give your users access to sets of objects, tabs, and other items all in one convenient bundle in the navigation bar.

Lightning apps let you brand your apps with a custom color and logo. You can even include a utility bar and Lightning page tabs in your Lightning app. Members of your org can work more efficiently by easily switching between apps. What’s most important to sales reps? Accounts, events, and organizations. How about sales managers? Reports and dashboards make the top of the list.

Let’s jump into the details.

Each Lightning app has a navigation bar at the top of the page, letting your users:

    Find what they need using item names for easy recognition
    Complete actions and access recent records and lists with a single click
    Personalize the navigation bar to suit the unique way they work

Think of the navigation bar as a container for a set of items and functionality. It’s always there, but the items within it change based on the app you’re using.

Lightning Navigation

    The app name (1) displays on the left side of the navigation bar and custom colors and branding make each app unique and easy to identify.
    Your users can access other items and apps by clicking the App Launcher icon (2).
    Your users can create records and access recent records and lists directly from the navigation bar (3) for items like Opportunities.

So what things can you put in a Lightning app?

    Most standard objects, including Home, the main Chatter feed, Groups, and People
    Your org’s custom objects
    Visualforce tabs
    Lightning component tabs
    Canvas apps via Visualforce tabs
    Web tabs

You can even include Lightning page tabs and utilities like Lightning Voice. If your org uses utility features, you can enable a utility bar in your app that allows instant access to productivity tools, like integrated voice, in the Lightning Experience footer.

You can also build your own on-demand apps by grouping items into new custom apps.

To switch between apps, users can use the App Launcher App Launcher icon. This makes it easy for users to switch contexts and still have access to the items, objects, and pages they need most.

App Launcher in Lightning Experience
Meet the Lightning Experience App Manager

The App Manager in Setup is your go-to place for managing apps for Lightning Experience. It shows all your connected apps and Salesforce apps.

Lightning Experience App Manager

Use the App Manager in Lightning Experience to:

    View all your Salesforce apps.
    Create Lightning apps or connected apps.
    See which apps are visible in Lightning Experience.
    Easily manage apps.

Note

Click a column header to sort the list based on that column.
What’s the Visible in Lightning Column About?

You can see in the App Manager that there are two types of apps: Classic and Lightning. A checkmark in the Visible in Lightning Experience column means that the app is accessible in Lightning Experience via the App Launcher and is fully functional.

Classic apps that don’t have a check mark in the Visible in Lightning column are enabled only for our Salesforce Classic UI. Because you’re working in Lightning Experience, you won’t find those Classic-only apps in the App Launcher. Classic apps marked as visible in Lightning Experience are fully usable in Lightning Experience, but they don’t take advantage of the app enhancements that Lightning Experience offers.
Create a Lightning App

Creating and editing a Lightning app is easy. As Ursa Major Solar’s admin, Maria needs an app that puts everything about customer energy assessments at her consultants’ fingertips. Let’s dive right in and try it out. In a few simple steps, you can give an app a name, set its primary color, upload a logo, specify which items appear in the app’s navigation bar, and assign the app to user profiles.

    From the Home tab in Setup, enter App

    in the Quick Find box, then select App Manager.
    Click New Lightning App. Walk through the Lightning App Wizard, creating an app with these parameters.
        App Name: Energy Consultations
        Description: Track energy audits and product recommendations.
        Image: Your choice! Use a JPG, PNG, BMP, or GIF image that’s smaller than 5 MB. For best results, upload an image that’s 128 by 128 pixels. Images larger than the maximum display of 128 by 128 pixels are automatically resized.
        Primary Hex Color Value: #FA8B05
        Org Theme Options: Select the checkbox.
        App Options and Utility Items: Leave as is.
        Navigation Items: Add these items in this order: Home, Chatter, Groups, Energy Audits, Accounts, Contacts, Products, Tasks
        If there are multiple Home tabs in the Available Items list, choose the one with the red icon.
        Assigned to user profile: System Administrator. Maria would assign it to her consultants’ user profile, but for our purposes, it’s easier to test if we set it to System Administrator.
    Click Save and Finish to exit the wizard.
    From the App Launcher App Launcher icon, find and select Energy Consultations.
    Finding Energy Consultations in the App Launcher
    Check out the new app! It’s got all the custom branding you gave it: a custom icon in the upper left and the custom color you assigned to it. Because Home is first in the navigation bar, it becomes the first page your users see when they open the app.

Sample App

Nice work! Now you’re ready to create your own custom Lightning apps.
Note

Did you know that app images for Lightning apps can be animated GIFs? Oh yes, they can. You're welcome.
Tips for Creating Apps in Lightning Experience

It’s time for the fun part: deciding how to set up Lightning apps for your users. Here are some tips for planning Lightning apps for your org.

Talk to your users. Ask them what their priorities are. Customizing tabs in apps gives you a unique opportunity to engage with your users. Each group of users has its own priorities. Find out which objects and items represent their highest priorities.

    Ask users to post feedback to a Chatter group.
    Publish polls.
    Schedule lunch sessions. Everyone likes a free lunch, and nearly everybody is happy to express their opinion.

Create a master list of objects that everyone in your org wants. Then trim down the list for each group—sales reps, sales managers, execs, and so on. The menus for every user group share some common objects, like Home, Tasks, and Feed. Keep the high-priority items for each group at the top. Put low-priority items at the bottom, or remove them altogether. Users can always go to the App Launcher to get the items they use less often.
Resources

    Salesforce Help: Salesforce App Considerations
    Salesforce Help: Personalized Navigation Considerations

Retake Quiz
This round is just for practice—you won’t earn more points or change your completion date. Now test your knowledge!
+100 Points Earned
Completed 7/19/2026
1
What's a key benefit (or benefits) of Lightning apps for your users?
A
Users can create records and access recent records and lists directly from the navigation bar.
B
It's easy to switch contexts with the App Launcher.
C
Lightning apps give users access to the items, objects, and pages they need most.
D
All of the above
2
What can you include in a Lightning app?
A
Unique scents that get released when a user clicks a button
B
Custom sound effects and flashing text
C
Web tabs, standard and custom objects, and utility features like Lightning Voice
D
All of the above
3
What's a good way to optimize an app for your users?
A
Brand the app with an animated GIF and neon colors to get their attention.
B
Put the highest priority objects and tabs first in the navigation menu.
C
Have a developer code in a sad trombone sound effect that plays for every error message.
D
Add every object in the org to the navigation menu.
