# Epidemiological-modelling-with-Markov-logic-networks
Bachelor Thesis: Epidemiological modelling in a university context - Evaluation of different protective measures using Markov logic networks

Because of the the globalisation and the growing population, diseases can spread more and more easily. A current example of this is the novel coronavirus SARS-CoV-2, which is affecting the whole world. In the case of a pandemic, protective measures are essential to reduce the rate of spread.  The goal of this work is to model the spread of a disease in a university context. In doing so, different protective measures will be evaluated in order to make face-to-face teaching as risk-free as possible.

The epidemiological modelling is implemented with Markov logic networks. The protective measures are then examined using data from my university. In the data set, the relationships between students, lectures and lecturers are stored. Statistical relational artificial intelligence is still a very new area of research. Especially the connection with the research area of epidemiology brings many opportunities.

RUN THE CODE:

The engine used for the MLN's is Tuffy. Tuffy relies on Java and PostgreSQL. Here you can find the download and a tutorial how to configure Tuffy with PostgreSQL:
http://i.stanford.edu/hazy/tuffy/doc/

the input of Tuffy consists of three parts: the MLN program, the evidence, and the query 
(you can find the INPUT in the directory samplesMLN)

java -jar tuffy.jar -i samples/coronaKi/prog.mln -e samples/samples/coronaKi/evidence.db
-queryFile samples/coronaKi/query.db -r out.txt

The OUTPUT is stored in: out.txt
