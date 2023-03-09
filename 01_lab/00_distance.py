#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {'Moscow': {'London': round(((sites['Moscow'][0] - sites['London'][0]) ** 2
                                         + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5
                                        , 2),
                        'Paris': round(((sites['Moscow'][0] - sites['Paris'][0]) ** 2
                                        + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** 0.5
                                       , 2),
                        },
             'London': {'Moscow': round(((sites['London'][0] - sites['Moscow'][0]) ** 2
                                         + (sites['London'][1] - sites['Moscow'][1]) ** 2) ** 0.5
                                        , 2),

                        'Paris': round(((sites['London'][0] - sites['Paris'][0]) ** 2
                                        + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5
                                       , 2),
                        },

             'Paris': {'Moscow': round(((sites['Paris'][0] - sites['Moscow'][0]) ** 2
                                        + (sites['Paris'][1] - sites['Moscow'][1]) ** 2) ** 0.5
                                       , 2),

                       'London': round(((sites['Paris'][0] - sites['London'][0]) ** 2
                                        + (sites['Paris'][1] - sites['London'][1]) ** 2) ** 0.5
                                       , 2),
                       }
             }

print(distances)