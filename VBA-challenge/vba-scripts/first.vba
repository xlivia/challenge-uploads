Sub typvchanges()
    Dim tsv As Double
    Dim pc As Double
    Dim yc As Double
    Dim tck As String
    Dim opn As Double
    Dim cls As Double
    Dim cellnum As Double
    cellnum = 2
    For i = 2 To 753001
        ' 2018:753001
        ' 2019:756001
        ' 2020:759001
        tsv = 0
        tck = Cells(i, 1).Value
        opn = Cells(i, 3).Value
        While (tck = Cells(i + 1, 1))
            tsv = tsv + Cells(i, 7).Value
            i = i + 1
        Wend
        cls = Cells(i, 6).Value
        yc = cls - opn
        pc = (yc / opn)
        tsv = tsv + Cells(i, 7).Value
        Cells(cellnum, 9).Value = tck
        Cells(cellnum, 10).Value = yc
        Cells(cellnum, 11).Value = Format(pc, "0.00%")
        Cells(cellnum, 12).Value = tsv
        If (yc < 0) Then
            Cells(cellnum, 10).Interior.ColorIndex = 3
        Else
            Cells(cellnum, 10).Interior.ColorIndex = 4
        End If
        cellnum = cellnum + 1
    Next i
End Sub