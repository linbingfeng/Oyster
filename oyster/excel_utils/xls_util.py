#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd


def read(file, end_col, sheets=0, nrows_start=1):
    data = xlrd.open_workbook(file)
    table = data.sheets()[sheets]
    nrows = table.nrows
    result = []
    for i in range(nrows_start, nrows):
        result.append(table.row_values(i)[:end_col])
    return result


def rows2json(rows, keys):
    results = []
    for row in rows:
        result = {}
        for i, col in enumerate(row):
            if isinstance(col, float):
                result[keys[i]] = int(col)
            else:
                result[keys[i]] = col.strip()
        results.append(result)
    return results

