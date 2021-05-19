"""
Nose tests
"""
import acp_times
import nose
import arrow

def test_200():
    assert str(acp_times.open_time(60, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T01:46"
    assert str(acp_times.close_time(60, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T04:00"
    assert str(acp_times.open_time(120, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T03:32"
    assert str(acp_times.close_time(120, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T08:00"
    assert str(acp_times.open_time(175, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T05:09"
    assert str(acp_times.close_time(175, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T11:40"
    assert str(acp_times.open_time(205, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T05:53"
    assert str(acp_times.close_time(205, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T13:30"

def test_300():
    assert str(acp_times.open_time(70, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T02:04"
    assert str(acp_times.close_time(70, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T04:40"
    assert str(acp_times.open_time(125, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T03:41"
    assert str(acp_times.close_time(125, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T08:20"
    assert str(acp_times.open_time(265, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T07:55"
    assert str(acp_times.close_time(265, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T17:40"
    assert str(acp_times.open_time(340, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T09:00"
    assert str(acp_times.close_time(340, 300, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T20:00"

def test_400():
    assert str(acp_times.open_time(90, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T02:39"
    assert str(acp_times.close_time(90, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T06:00"
    assert str(acp_times.open_time(175, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T05:09"
    assert str(acp_times.close_time(175, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T11:40"
    assert str(acp_times.open_time(240, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T07:08"
    assert str(acp_times.close_time(240, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T16:00"
    assert str(acp_times.open_time(390, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T11:49"
    assert str(acp_times.close_time(390, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T02:00"
    assert str(acp_times.open_time(460, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T12:08"
    assert str(acp_times.close_time(460, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T03:00"

def test_600():
    assert str(acp_times.open_time(100, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T02:56"
    assert str(acp_times.close_time(100, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T06:40"
    assert str(acp_times.open_time(200, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T05:53"
    assert str(acp_times.close_time(200, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T13:20"
    assert str(acp_times.open_time(300, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T09:00"
    assert str(acp_times.close_time(300, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T20:00"
    assert str(acp_times.open_time(400, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T12:08"
    assert str(acp_times.close_time(400, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T02:40"
    assert str(acp_times.open_time(500, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T15:28"
    assert str(acp_times.close_time(500, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T09:20"
    assert str(acp_times.open_time(600, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T18:48"
    assert str(acp_times.close_time(600, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T16:00"
    assert str(acp_times.open_time(700, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T18:48"
    assert str(acp_times.close_time(700, 600, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T16:00"

def test_1000():
    assert str(acp_times.open_time(45, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T01:19"
    assert str(acp_times.close_time(45, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T03:15"
    assert str(acp_times.open_time(147, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T04:19"
    assert str(acp_times.close_time(147, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T09:48"
    assert str(acp_times.open_time(295, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T08:51"
    assert str(acp_times.close_time(295, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T19:40"
    assert str(acp_times.open_time(328, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T09:53"
    assert str(acp_times.close_time(328, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T21:52"
    assert str(acp_times.open_time(590, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T18:28"
    assert str(acp_times.close_time(590, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T15:20"
    assert str(acp_times.open_time(890, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T05:09"
    assert str(acp_times.close_time(890, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-03T17:23"
    assert str(acp_times.open_time(1190, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T09:05"
    assert str(acp_times.close_time(1180, 1000, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-04T03:00"

def test_close_200_400():
    assert str(acp_times.close_time(200, 200, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-01T13:30"
    assert str(acp_times.close_time(400, 400, arrow.get('2021-01-01T00:00')).format('YYYY-MM-DDTHH:mm')) == "2021-01-02T03:00"
