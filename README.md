 TEAM 23
Participants of the Team 23:
1. Askar Akhmetkhanov (SD - 03) 2. Aleksei Kureikin (CBS-01)
3. Arseny Savchenko (CBS-01) 4. Said Nurullin (GD-01)
5. Mikhail Stepanov (GD - 01)
Hands-on: Message Brokers
Githubs:
1) https://github.com/dinaraparanid/MQToEmail - Publish Service
2) https://github.com/SaidNurullin/SoftArchScreamingService - SCREAMING Service 3) https://github.com/AskArtwentythree/filter-service - Filter Service
4) https://github.com/AlexeyKureykin/message_brokers - User-facing REST API
5) https://github.com/Reelap13/SA2024_PaF - Pipes-and-Filters
Video demonstrations: https://rutube.ru/video/private/b453fa8b3777ace74baba3b1a126e725/?p=ZSR0QAvHU0EQlj DEOamzjg - Pipes-and-Filters
https://rutube.ru/video/private/97308b2c4064bc12b3e94657260731de/?p=_78OPRlWeufy_9 p34WldaA - Event-Driven variations
Report
In Pipes-and-filters tests, delays are between 1.22 to 1.29 seconds per message because of synchronous processing. While event-driven tests showed faster message processing (from 594 ms to 927 ms) because of asynchronous handling.
Event-driven systems, while fault-tolerant, require more RAM because of independent services and constant RabbitMQ connections. This makes sure that the failures in one service don't break others, but also increases resource usage. On the other hand, pipes-and-filters are efficient in resource usage, as all functions run sequentially in one service, reducing memory usage. However, this approach affects fault tolerance in the way that the approach weakens it since a failure in one part stops the entire pipeline. Generally, the choice depends on whether the system prioritizes resource efficiency or persistence.
         
