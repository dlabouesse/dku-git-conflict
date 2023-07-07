# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

git_tmp_df = pd.DataFrame({"a": [43]})


# Write recipe outputs
git_tmp = dataiku.Dataset("git_tmp")
git_tmp.write_with_schema(git_tmp_df)
