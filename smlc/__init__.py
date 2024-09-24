"""Simple Machine Learning Cooperation.

>>> from pprint import pp as print
>>> import mlcroissant as mlc
>>> fraud_dataset = mlc.Dataset('https://www.kaggle.com/datasets/lnasiri007/ieeecis-fraud-detection/croissant/download')
>>> print(fraud_dataset.operations.issues.report())
('Found the following 1 warning(s) during the validation:\\n'
 '  -  [Metadata(IEEE-CIS FRAUD DETECTION)] Property '
 '"http://mlcommons.org/croissant/citeAs" is recommended, but does not exist.')
>>> print([n for n in fraud_dataset.operations.operations.nodes])
[Download(archive.zip),
 Extract(archive.zip),
 Read(sample_submission.csv_fileobject),
 Read(test_identity.csv_fileobject),
 Read(test_transaction.csv_fileobject),
 Read(train_identity.csv_fileobject),
 Read(train_transaction.csv_fileobject),
 ReadFields(sample_submission.csv),
 ReadFields(test_identity.csv),
 ReadFields(test_transaction.csv),
 ReadFields(train_identity.csv),
 ReadFields(train_transaction.csv),
 InitOperation(_:...)]
>>> print(fraud_dataset.operations.operations.entry_operations())
[InitOperation(_:...)]
>>> fraud_metadata = fraud_dataset.metadata
>>> fraud_metadata.keywords
['subject > people and society > law > government > public safety']
>>> fraud_metadata.publisher[0].name, fraud_metadata.publisher[0].url
('Kaggle', 'https://www.kaggle.com/organizations/kaggle')
>>> print(fraud_metadata.distribution)  # file objects and file sets
[FileObject(uuid="archive.zip"),
 FileObject(uuid="sample_submission.csv_fileobject"),
 FileObject(uuid="test_identity.csv_fileobject"),
 FileObject(uuid="test_transaction.csv_fileobject"),
 FileObject(uuid="train_identity.csv_fileobject"),
 FileObject(uuid="train_transaction.csv_fileobject")]
>>> fraud_metadata.distribution[0].name, fraud_metadata.distribution[0].description
('archive.zip', 'Archive containing all the contents of the IEEE-CIS FRAUD DETECTION dataset')
>>> fraud_metadata.distribution[0].encoding_format, fraud_metadata.distribution[0].content_size
('application/zip', '118.119 MB')
>>> fraud_metadata.distribution[-1].name, fraud_metadata.distribution[-1].description
('train_transaction.csv', None)
>>> fraud_metadata.distribution[-1].encoding_format, fraud_metadata.distribution[-1].content_size
('text/csv', None)
>>> print(fraud_metadata.record_sets)
[RecordSet(uuid="sample_submission.csv"),
 RecordSet(uuid="test_identity.csv"),
 RecordSet(uuid="test_transaction.csv"),
 RecordSet(uuid="train_identity.csv"),
 RecordSet(uuid="train_transaction.csv")]
>>> sample_record_set = fraud_metadata.record_sets[0]
>>> sample_record_set.name, sample_record_set.description
('sample_submission.csv', None)
>>> sample_record_set.fields
[Field(uuid="sample_submission.csv/TransactionID"), Field(uuid="sample_submission.csv/isFraud")]
>>> sample_record_set.fields[0].name, sample_record_set.fields[0].data_types, sample_record_set.fields[0].data_type
('TransactionID', [rdflib.term.URIRef('https://schema.org/Text')], <class 'bytes'>)
>>> sample_record_set.fields[1].name, sample_record_set.fields[1].data_types, sample_record_set.fields[1].data_type
('isFraud', [rdflib.term.URIRef('https://schema.org/Float')], <class 'float'>)
>>> sample_record_set.fields[0].parent_field, sample_record_set.fields[0].sub_fields
(None, [])
>>> # These require further investigation
>>> fraud_metadata.data_imputation_protocol
>>> fraud_metadata.data_preprocessing_protocol
>>> fraud_metadata.data_manipulation_protocol
>>> fraud_metadata.data_use_cases
>>> fraud_metadata.data_limitations
>>> # Especially this one
>>> fraud_metadata.personal_sensitive_information
>>> # JSON(LD) serialization
>>> import json
>>> from datetime import datetime
>>> handle_dttm = lambda x: x.isoformat() if isinstance(x, datetime) else x
>>> json.dumps(fraud_metadata.to_json(), default=handle_dttm)
'{...}'
"""

__docformat__ = "numpy"


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
