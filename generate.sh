#!/bin/bash

LANG=python

swagger-codegen generate \
	-i public.yaml \
	-l $LANG \
	-o "."

