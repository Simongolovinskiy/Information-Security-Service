import React, { useEffect, useState } from 'react'
import classes from "./Result.module.css"
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
} from '@chakra-ui/react'
import { useGetResult } from '../../api/queries.js'
import axios from 'axios'
import TableElements from '../tableel/TableElements.jsx'
export default function Result() {

  const [page, setPage] = useState(1)
  const [dataSet, setDataSet] = useState([])
  const [range, setRange] = useState(1)
  const [numberPage, setNumberPage] = useState(1)

  const {data: resultData} = useGetResult()

  /* useEffect(() => {
    async function fetchData(){
      await axios.get("http://localhost:8000/api/lstm/")
      .then(res => res.data)
      .then(res => setDataSet(res))
    }
    fetchData()
  }, []) */

  useEffect(() => {
    if(resultData){
      setDataSet(resultData)
    }
  }, [resultData])

  const handlePage = (page_id) => {
    setPage(page_id)
  }

  const handleChangeRangeValue = (val) => {
    setRange(val)
    setNumberPage(+val)
    setPage(+val)
  }

  const handleChangeNumberValue = (val) => {
    let valRestricted = val.replace(/[A-Z a-z]/g, 1)
    if(+valRestricted > dataSet.length){
      return
    }
    setRange(valRestricted)
    setNumberPage(+valRestricted)
    setPage(+valRestricted)

  }

  return (
    <div id="res" className='wrapper'>
      <div className={classes.resultBody}>
      <h2>Таблица свежих данных</h2>
      <div className={classes.rangeInput}>
        <input type="range" min={1} step={1} max={dataSet?.length} value={range} onChange={e => handleChangeRangeValue(e.target.value)}/>
        {range}
      </div>
      <div className={classes.inputNumber}>
        <input type="text" value={numberPage} onChange={e => handleChangeNumberValue(e.target.value)} />
      </div>
      {/* <div className={classes.paginationBullets}>
          {
            dataSet?.map(item => (
              <div onClick={() => handlePage(item.id)} className={`${classes.paginationBulletItem} ${item.id === page && classes.activePage} ${item.is_threat === "true" && classes.threat}`}>{item.id}</div>
            ))
          }
      </div> */}
      <TableContainer>
        <Table variant='simple'>
          <TableCaption>Все данные в реальном времени</TableCaption>
          <Thead>
            <Tr>
              <Th>Показатель</Th>
              <Th>Значение</Th>
            </Tr>
          </Thead>
          <Tbody>
              {dataSet?.length > 0 && 
              dataSet
              ?.filter(item => item.id === page)
              ?.map((item, index) => (
                <TableElements key={index} value={item} />  
              ))
              }
          </Tbody>
          <Tfoot>
            <Tr>
              <Th>Показатель</Th>
              <Th>Значение</Th>
            </Tr>
          </Tfoot>
        </Table>
      </TableContainer>
      </div>
    </div>
  )
}
