<h1>Zombies on Campus</h1>

Please view a running version of the project from the following url:
http://zombiesoncampus.pythonanywhere.com

<h2>About</h2>

<p>Zombies on Campus is a quick fun choice-based game where a user can play a variety of stories and make choices that affect the ending.</p>

<p>The development team</p>

<ul>
            <li>Shallu Gangwani, MSc IT <a href="https://github.com/2165738G" target="_blank"> GitHub</a> <a href="mailto:2165738G@student.gla.ac.uk" target="_blank"><span class="glyphicon glyphicon-envelope"></span> Mail</a></li>
            <li>Konstantinos Kagiampakis, MSc SE <a href="https://github.com/kostiskag" target="_blank"> GitHub</a> <a href="mailto:kostiskag@gmail.com" target="_blank"><span class="glyphicon glyphicon-envelope"></span> Mail</a></li>
            <li>Simonas Viliunas, MSc SD <a href="https://github.com/vilisimo" target="_blank"> GitHub</a>
            </li><li>Laura Zebrauskaite, MSc SD <a href="https://github.com/laurabzz" target="_blank"> GitHub</a></li>
</ul>

<p>University of Glasgow, March 2016</p>

<p>We would like to thank our lecturer Dr Leif Azzopardi <a href="http://www.dcs.gla.ac.uk/~leif/" target="_blank"><span class="glyphicon glyphicon-globe"></span> web</a> for his guidance and his valuable online guide <a href="http://www.tangowithdjango.com/"><span class="glyphicon glyphicon-globe"></span> Tango With Django </a>.
</p>


<p>The project was built with the help of a variety of technologies</p>

<ul>
            <li>Python <a href="https://www.python.org/"><span class="glyphicon glyphicon-globe"></span> web</a></li>
            <li>Django <a href="https://www.djangoproject.com/"><span class="glyphicon glyphicon-globe"></span> web</a></li>
            <li>jQuery <a href="https://jquery.com/"><span class="glyphicon glyphicon-globe"></span> web</a></li>
            <li>Bootstrap <a href="http://getbootstrap.com/"><span class="glyphicon glyphicon-globe"></span> web</a></li>
            <li>Chart.js <a href="http://www.chartjs.org/"><span class="glyphicon glyphicon-globe"></span> web</a></li>
        </ul>


<h2>Install</h2>

<ul>
<li>git clone ...</li>
<li>cd ...</li>
<li>mkvirtualenv zombies</li>
<li>workon zombies</li>
<li>pip install -r requirements.txt</li>
</ul>

<h3>Run Server</h3>
python manage.py runserver

<h3>Populate Stories</h3>
There is an allready populated database, in case you want to repopulate remove database entries
and do

<ul>
<li>python manage.py migrate</li>
<li>python populate_users_stories.py</li>
<p>Note that the population script will also create the users (with superuser privileges).</p>
</ul>

