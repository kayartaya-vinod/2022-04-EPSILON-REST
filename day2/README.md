-   REST API - pattern for data/information exchange between client app and server app.
-   No standards, only convensions and guides
-   Based on 6 constraints defined by Roy Fielding
-   CRUD - Cread, Read, Upate, and Delete (basic operations of a persistence mechanism)
-   POST, GET, PUT (or PATCH), DELETE - HTTP methods that correspond to CRUD operations
-   SOA - Service Oriented Architecture
    -   SOAP - Simple Object Access Protocol (no longer an acronym) (Big web service)
    -   REST - Representational State Transfer
-   XML - Extensible Markup Language, standardized by W3C - used for data representation
-   JSON - JavaScript Object Notation - Widely accepted format, easy to represent and convert to other languages


```xml
<?xml version="1.0" ?>

<book lang="EN">
    <id>7689</id>
    <title>REST in simple English</title>
    <no-of-pages>290</no-of-pages>
    <price>
        <currency>INR</currency>
        <value>499</value>
    </price>
    <authors>
        <author>Vinod Kumar</author>
        <author>Shyam Sundar</author>
    </authors>
</book>
```

```json
{
    "lang": "EN",
    "id": 7689,
    "title": "REST in simple English",
    "noOfPages": 290,
    "price": {
        "currency": "INR",
        "value": 499
    },
    "authors": [
        "Vinod Kumar", "Shyam Sundar"
    ]
}

```