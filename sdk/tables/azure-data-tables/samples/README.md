---
page_type: sample
languages:
  - python
products:
  - azure
  - azure-table-storage
urlFragment: tables-samples
---

# Samples for Azure Tables client library for Python

These code samples show common scenario operations with the Azure Data Tables client library.

You can authenticate your client with a Tables API key:
* See [sample_authentication.py][sample_authentication] and [sample_authentication_async.py][sample_authentication_async] for how to authenticate in the above cases.

These sample programs show common scenarios for the Tables client's offerings.

|**File Name**|**Description**|
|-------------|---------------|
|[sample_create_client.py][create_client] and [sample_create_client_async.py][create_client_async]|Instantiate a table client|Authorizing a `TableServiceClient` object and `TableClient` object|
|[sample_create_delete_table.py][create_delete_table] and [sample_create_delete_table_async.py][create_delete_table_async]|Creating and deleting a table in a storage account|
|[sample_insert_delete_entities.py][insert_delete_entities] and [sample_insert_delete_entities_async.py][insert_delete_entities_async]|Inserting and deleting individual entities in a table|
|[sample_query_tables.py][query_tables] and [sample_query_tables_async.py][query_tables_async]|Querying tables in a storage account|
|[sample_update_upsert_merge_entities.py][update_upsert_merge] and [sample_update_upsert_merge_entities_async.py][update_upsert_merge_async]| Updating, upserting, and merging entities|
|[sample_batching.py][sample_batch] and [sample_batching_async.py][sample_batch_async]| Committing many requests in a single batch|
|[sample_copy_table.py][sample_copy_table] and [sample_copy_table_async.py][sample_copy_table_async]| Copying a table between Tables table and Storage blob|
|[sample_get_entity_etag_and_timestamp.py][sample_get_entity_etag_and_timestamp] and [sample_get_entity_etag_and_timestamp_async.py][sample_get_entity_etag_and_timestamp_async]| Getting entity's etag and timestamp|


### Prerequisites
* Python 3.8 or later is required to use this package.
* You must have an [Azure subscription](https://azure.microsoft.com/free/) and either an
[Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-overview) or an [Azure Cosmos Account](https://learn.microsoft.com/azure/cosmos-db/account-overview) to use this package.

## Setup

1. Install the Azure Data Tables client library for Python with [pip](https://pypi.org/project/pip/):
```bash
pip install --pre azure-data-tables
```
2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Running the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. Follow the usage described in the file, e.g. `python sample_create_table.py`

## Writing Filters

### Supported Comparison Operators
|**Operator**|**URI expression**|
|------------|------------------|
|`Equal`|`eq`|
|`GreaterThan`|`gt`|
|`GreaterThanOrEqual`|`ge`|
|`LessThan`|`lt`|
|`LessThanOrEqual`|`le`|
|`NotEqual`|`ne`|
|`And`|`and`|
|`Not`|`not`|
|`Or`|`or`|

### Formatting and quote characters

Query strings must wrap literal values in single quotes. Literal values containing single quote characters must be escaped with a double single quote.
```python
query_filter = "LastName eq 'O''Connor' and CustomerSince eq datetime'2008-07-10T00:00:00Z'"
table_client.query_entities(query_filter)
```
Query strings can also be parameterized using a dictionary of values, which will be automatically formatted with single quotes according to data type.
When using the parameter dictionary to format filters, any single quote characters in the values will be automatically escaped.
```python
parameters = {
    "last_name": "O'Connor",
    "customer_since": datetime(year=2008, month=7, day=10)
}
query_filter = "LastName eq @last_name and CustomerSince eq @customer_since"
table_client.query_entities(query_filter, parameters=parameters)
```

For more information on formatting and supported characters, please see the [query reference documentation][query_reference_documentation].


### Example Filters

#### Filter on `PartitionKey` and `RowKey`:
```python
parameters = {
    "pk": PartitionKey,
    "rk": RowKey
}
query_filter = "PartitionKey eq @pk and RowKey eq @rk"
table_client.query_entities(query_filter, parameters=parameters)
```

#### Filter on Properties
```python
parameters = {
    "first": first_name,
    "last": last_name
}
query_filter = "FirstName eq @first or LastName eq @last"
table_client.query_entities(query_filter, parameters=parameters)
```

#### Filter with string comparison operators
```python
query_filter = "LastName ge 'A' and LastName lt 'B'"
table_client.query_entities(query_filter)
```

#### Filter with numeric properties
```python
query_filter = "Age gt 30"
table_client.query_entities(query_filter)
```

```python
query_filter = "AmountDue le 100.25"
table_client.query_entities(query_filter)
```

#### Filter with boolean properties
```python
query_filter = "IsActive eq true"
table_client.query_entities(query_filter)
```

#### Filter with DateTime properties
```python
query_filter = "CustomerSince eq datetime'2008-07-10T00:00:00Z'"
table_client.query_entities(query_filter)
```

#### Filter with GUID properties
```python
query_filter = "GuidValue eq guid'a455c695-df98-5678-aaaa-81d3367e5a34'"
table_client.query_entities(query_filter)
```


## Next steps

Check out the [API reference documentation][api_reference_documentation] to learn more about
what you can do with the Azure Data Tables client library.


<!-- LINKS -->
[api_reference_documentation]: https://learn.microsoft.com/rest/api/storageservices/table-service-rest-api
[query_reference_documentation]: https://learn.microsoft.com/rest/api/storageservices/querying-tables-and-entities

[sample_authentication]:https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_authentication.py
[sample_authentication_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_authentication_async.py

[create_client]:https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_create_client.py
[create_client_async]:https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_create_client_async.py

[create_delete_table]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_create_delete_table.py
[create_delete_table_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_create_delete_table_async.py

[insert_delete_entities]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_insert_delete_entities.py
[insert_delete_entities_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_insert_delete_entities_async.py

[query_entities]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_query_table.py
[query_table_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_query_table_async.py

[query_tables]:https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_query_tables.py
[query_tables_async]:https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_query_tables_async.py

[update_upsert_merge]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_update_upsert_merge_entities.py
[update_upsert_merge_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_update_upsert_merge_entities_async.py

[sample_batch]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_batching.py
[sample_batch_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_batching_async.py

[sample_copy_table]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_copy_table.py
[sample_copy_table_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_copy_table_async.py

[sample_get_entity_etag_and_timestamp]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/sample_get_entity_etag_and_timestamp.py
[sample_get_entity_etag_and_timestamp_async]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples/async_samples/sample_get_entity_etag_and_timestamp_async.py

